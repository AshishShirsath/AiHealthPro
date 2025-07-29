from flask import Flask, request, jsonify, render_template_string
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",  
    api_key="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"  
)

@app.route("/")
def index():

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>News Chatbot</title>
        <style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: linear-gradient(to bottom right, #6a11cb, #2575fc); /* Blue gradient */
        color: #fff;
    }

    .chat-container {
        width: 90%;
        max-width: 600px;
        height: 75vh;
        background: rgba(255, 255, 255, 0.9); /* White with transparency */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2); /* Stronger shadow for a floating effect */
        border-radius: 15px; /* More rounded corners for a modern look */
        padding: 20px;
        display: flex;
        flex-direction: column;
    }

    .chat-box {
        flex: 1;
        overflow-y: auto;
        padding: 15px;
        border-bottom: 2px solid #ddd;
        border-radius: 10px 10px 0 0;
        background: #f9f9f9;
    }

    .chat-message {
        margin: 10px 0;
        display: flex;
        align-items: center;
    }

    .user-message {
        text-align: right;
        color: #1e3799;
        font-weight: bold;
    }

    .user-message strong {
        color: #1e3799;
    }

    .bot-message {
        text-align: left;
        color: #38ada9;
    }

    .bot-message strong {
        color: #38ada9;
    }

    input[type="text"] {
        width: 100%;
        padding: 15px; /* Increased padding for a better typing experience */
        border: 2px solid #ddd;
        border-radius: 10px;
        margin-top: 10px;
        font-size: 16px; /* Larger font size for readability */
    }

    button {
        background: linear-gradient(to right, #6a11cb, #2575fc); /* Gradient button */
        color: white;
        padding: 12px 25px; /* Adjusted for comfort */
        border: none;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        margin-top: 10px;
        transition: background 0.3s ease;
    }

    button:hover {
        background: linear-gradient(to right, #2575fc, #6a11cb); /* Hover effect: reverse gradient */
    }

    @media (max-width: 768px) {
        .chat-container {
            width: 95%;
            height: 80vh;
        }
    }

    @media (max-width: 480px) {
        button {
            font-size: 14px;
            padding: 10px 20px;
        }

        input[type="text"] {
            font-size: 14px;
        }
    }
</style>
    </head>
    <body>
        <div class="chat-container">
            <div class="chat-box" id="chatbox">
                <!-- Chat messages will appear here -->
            </div>
            <input type="text" id="userMessage" placeholder="Ask a news related question..." />
            <button onclick="sendMessage()">Send</button>
        </div>
        <script>
            async function sendMessage() {
                const userMessage = document.getElementById("userMessage").value.trim();
                if (!userMessage) return;

                // Display user's message
                const chatBox = document.getElementById("chatbox");
                chatBox.innerHTML += `<div class="user-message"><strong>You:</strong> ${userMessage}</div>`;

                try {
                    // Send the message to the Flask backend
                    const response = await fetch("/chat", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ message: userMessage })
                    });

                    const data = await response.json();

                    // Display bot's reply
                    if (data.reply) {
                        chatBox.innerHTML += `<div class="bot-message"><strong>Bot:</strong> ${data.reply}</div>`;
                    } else {
                        chatBox.innerHTML += `<div class="bot-message"><strong>Bot:</strong> Sorry, I didn't understand that.</div>`;
                    }
                } catch (error) {
                    chatBox.innerHTML += `<div class="bot-message"><strong>Bot:</strong> There was an error: ${error.message}</div>`;
                }

                // Clear the input field
                document.getElementById("userMessage").value = "";

                // Scroll to the latest message
                chatBox.scrollTop = chatBox.scrollHeight;
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        completion = client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-70b-instruct", 
            messages=[{"role": "user", "content": user_input}],
            temperature=0.5,
            top_p=1,
            max_tokens=1024
        )

        ai_reply = completion.choices[0].message.content

        return jsonify({"reply": ai_reply})

    except Exception as e:
        print(f"Error: {e}")  
        return jsonify({"error": str(e)}), 500
        


if __name__ == "__main__":
    app.run(debug=True, port=9111)
