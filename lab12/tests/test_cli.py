import json
import subprocess
import pytest

CLI_CMD = ["python", "-m", "src.async_tool"]

def create_input_file(tmp_path, data):
    """Helper function to create a temporary JSON file with test data."""
    input_file = tmp_path / "input.json"
    input_file.write_text(json.dumps(data))
    return str(input_file)

def test_basic_execution(tmp_path):
    """1. Basic execution: program exits with code 0, output is valid JSON."""
    data = [{"id": 1, "delay": 0.1, "good": True}]
    input_path = create_input_file(tmp_path, data)
    
    result = subprocess.run(CLI_CMD + [input_path], capture_output=True, text=True, timeout=5)
    
    assert result.returncode == 0
    output = json.loads(result.stdout)
    assert len(output) == 1
    assert output[0]["status"] == "done"

def test_mode_behavior(tmp_path):
    """2. Mode behavior: test non-default mode (async)."""
    data = [
        {"id": 1, "delay": 0.1, "good": True},
        {"id": 2, "delay": 0.1, "good": True}
    ]
    input_path = create_input_file(tmp_path, data)
    
    result = subprocess.run(CLI_CMD + [input_path, "--mode", "async"], capture_output=True, text=True, timeout=5)
    
    assert result.returncode == 0
    output = json.loads(result.stdout)
    assert len(output) == 2

def test_error_without_flag(tmp_path):
    """3. Error without flag: failing task causes non-zero exit code."""
    data = [{"id": 1, "delay": 0.1, "good": False}]
    input_path = create_input_file(tmp_path, data)
    
    result = subprocess.run(CLI_CMD + [input_path], capture_output=True, text=True, timeout=5)
    
    assert result.returncode != 0

def test_error_with_flag(tmp_path):
    """4. Error with flag: program doesn't crash, failed task has 'error' status."""
    data = [
        {"id": 1, "delay": 0.1, "good": False},
        {"id": 2, "delay": 0.1, "good": True}
    ]
    input_path = create_input_file(tmp_path, data)
    
    result = subprocess.run(CLI_CMD + [input_path, "--continue-on-error"], capture_output=True, text=True, timeout=5)
    
    assert result.returncode == 0
    output = json.loads(result.stdout)
    assert len(output) == 2
    
    assert output[0]["id"] == 1
    assert output[0]["status"] == "error"
    assert "message" in output[0]
    
    assert output[1]["id"] == 2
    assert output[1]["status"] == "done"

def test_output_structure(tmp_path):
    """5. Output structure: result is JSON, item count matches, order is preserved."""
    data = [
        {"id": 5, "delay": 0.1, "good": True},
        {"id": 3, "delay": 0.1, "good": True}
    ]
    input_path = create_input_file(tmp_path, data)
    
    result = subprocess.run(CLI_CMD + [input_path, "--mode", "sync"], capture_output=True, text=True, timeout=5)
    
    assert result.returncode == 0
    output = json.loads(result.stdout)
    
    assert isinstance(output, list)
    assert len(output) == len(data)
    assert output[0]["id"] == 5
    assert output[1]["id"] == 3