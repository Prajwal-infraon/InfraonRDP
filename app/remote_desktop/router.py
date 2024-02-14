from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse, FileResponse
from .controller import *
from .models import * 
from .utility import *
rdp_router = APIRouter()


@rdp_router.post("/get-url")
def getUrl(node_info : NodeInfoRequest):
    url = ""
    try:
        url = processForUrl(node_info)
    except Exception as e:
        print(">>>>",e)
    return JSONResponse(url)

@rdp_router.post("/get-agent")
def getAgent(exe_info : AgentExeRequest):
    exe_agent = getAgentexe(exe_info)
    return exe_agent


@rdp_router.get("/get-file")
async def downloadAgent(file_name):
    file_name = decode_file_name(file_name)
    filepath =f'C:/Users/infraon/Desktop/remote_desktop_api/Agents/{file_name}'
    return FileResponse(filepath, media_type='application/octet-stream',filename=file_name)

@rdp_router.post("/receive_data")
async def receive_data(request: Request):
    try:
        data = await request.json()
        organization = data.get('organization_id', '')
        serial_number = data.get('serial_number', '')
        print("Received data from Django REST API:", organization, serial_number)
        return {"status": "success", "message": "Data received successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")
    
# @rdp_router.get("/get-shfile")
# async def getShFile():#mesh_id
#     return shfile()