import uvicorn
import sys

sys.dont_write_bytecode = True

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)