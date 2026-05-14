import pytest
from src.async_tool.__main__ import process_item

@pytest.mark.asyncio
async def test_process_item_success():
    """Test success scenario: valid input returns the correct result."""
    item = {"id": 1, "delay": 0.1, "good": True}
    result = await process_item(item)
    
    assert result["id"] == 1
    assert result["status"] == "done"

@pytest.mark.asyncio
async def test_process_item_failure():
    """Test failure scenario: good=False raises a ValueError."""
    item = {"id": 2, "delay": 0.1, "good": False}
    
    with pytest.raises(ValueError, match="Task 2 failed"):
        await process_item(item)

@pytest.mark.asyncio
async def test_process_item_structure():
    """Test basic correctness: result structure matches the expected format."""
    item = {"id": 3, "delay": 0.0, "good": True}
    result = await process_item(item)
    
    assert "id" in result
    assert "status" in result
    assert isinstance(result["id"], int)
    assert isinstance(result["status"], str)