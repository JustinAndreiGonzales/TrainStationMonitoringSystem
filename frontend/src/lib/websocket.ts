export function connectWebSocket(station_id: string, platform_side: string, onMessage: (data: any) => void) {
    const socket = new WebSocket(`wss://trenph.up.railway.app/ws/eta/${station_id}/${platform_side}/`);
    console.log("Attempting to connect WebSocket to:", socket);
    
    socket.onmessage = (event) => {
        try {
            const data = JSON.parse(event.data);
            onMessage(data);
        } catch (error) {
            console.error("WebSocket message error:", error);
        }
    };

    socket.onopen = () => console.log("WebSocket Connected!");
    socket.onerror = (err) => console.error("WebSocket Error:", err);
    socket.onclose = () => console.log("WebSocket Closed!");

    return socket;
}
