import json
import websocket


def run_vscode(cmd: str, args: list[str] | None = None, hostname: str = "localhost", port: int = 3710):
    """
    Connect to a VSCode WebSocket server and execute a command.
    
    Args:
        cmd: The command ID to execute (e.g., "command.id.with.arguments")
        args: Optional list of arguments to pass to the command
        hostname: The hostname of the WebSocket server (default: "localhost")
        port: The port of the WebSocket server (default: 3710)
    
    Returns:
        The response from the server, if any
    
    Example:
        run_vscode("workbench.action.files.newFile")
        run_vscode("command.id.with.arguments", args=["value"])
    """
    # Construct the WebSocket URL
    ws_url = f"ws://{hostname}:{port}"
    
    # Prepare the message payload
    message = {
        "command": cmd,
        "args": args if args is not None else []
    }
    
    # Connect to the WebSocket server and send the command
    ws = websocket.create_connection(ws_url)
    try:
        # Send the JSON message
        ws.send(json.dumps(message))
        
        # Wait for and return the response
        response = ws.recv()
        return response
    finally:
        ws.close() # context manager not supported

