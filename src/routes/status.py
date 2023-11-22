from fastapi import APIRouter, Query
from src.controllers.StatusController import StatusController
from src.schemas.status import ApiResponse

# prefix="/discover",
router = APIRouter(tags=['Agent Status'])

@router.get('/status', response_model=ApiResponse)
def discover(id: str = Query(..., description="Task ID")):
  return StatusController.get_status(id)
