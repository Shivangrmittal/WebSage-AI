// ======================================================
// AI Webpage Assistant - popup.js
// ======================================================

// ===============================
// Current Page Information
// ===============================

const titleElement = document.getElementById("title");
const urlElement = document.getElementById("url");
let currentPageURL = "";

chrome.tabs.query(
    {
        active: true,
        currentWindow: true
    },
    (tabs) => {

        const currentTab = tabs[0];

        currentPageURL = currentTab.url;

        titleElement.textContent = currentTab.title;

        try {

            const url = new URL(currentTab.url);

            let domain = url.hostname;

            // Remove "www."
            domain = domain.replace(/^www\./, "");

            urlElement.textContent = `🌐 ${domain}`;

        }

        catch {

            urlElement.textContent = currentTab.url;

        }

    }
);

// ===============================
// Chat Elements
// ===============================

const chatContainer = document.getElementById("chat-container");
const questionInput = document.getElementById("question");
const sendButton = document.getElementById("sendBtn");

// ===============================
// Welcome Message
// ===============================

addMessage(
    "bot",
    "👋 Hi! Ask me anything about the webpage you're currently viewing."
);

// ===============================
// Add Message
// ===============================

function addMessage(sender, message) {

    const messageDiv = document.createElement("div");

    if (sender === "user") {

        messageDiv.className = "user-message";

        messageDiv.innerHTML = `
            <strong>👤 You</strong><br><br>
            ${message}
        `;

    } else {

        messageDiv.className = "ai-message";

        messageDiv.innerHTML = `
            <strong>🤖 AI</strong><br><br>
            ${message}
        `;

    }

    chatContainer.appendChild(messageDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// ===============================
// Show Loading
// ===============================

function showLoading() {

    const loadingDiv = document.createElement("div");

    loadingDiv.className = "ai-message";

    loadingDiv.id = "loading";

    loadingDiv.innerHTML = `
        <strong>🤖 AI</strong><br><br>
        Thinking...
    `;

    chatContainer.appendChild(loadingDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// ===============================
// Remove Loading
// ===============================

function removeLoading() {

    const loading = document.getElementById("loading");

    if (loading) {
        loading.remove();
    }

}

// ===============================
// Send Message
// ===============================

async function sendMessage() {

    const question = questionInput.value.trim();

    if (question === "") {
        return;
    }

    // Display user message
    addMessage("user", question);

    // Clear input
    questionInput.value = "";

    // Disable controls
    questionInput.disabled = true;
    sendButton.disabled = true;
    sendButton.textContent = "Thinking...";

    // Show loading bubble
    showLoading();

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question,
                    url: currentPageURL
                })
            }
        );

        removeLoading();

        if (!response.ok) {

            addMessage(
                "bot",
                `❌ Backend Error (${response.status})`
            );

            return;
        }

        const data = await response.json();

        addMessage("bot", data.answer);

    }

    catch (error) {

        removeLoading();

        addMessage(
            "bot",
            "❌ Could not connect to the backend.\n\nMake sure FastAPI is running."
        );

        console.error(error);

    }

    finally {

        questionInput.disabled = false;
        sendButton.disabled = false;

        sendButton.textContent = "Send";

        questionInput.focus();

    }

}

// ===============================
// Button Click
// ===============================

sendButton.addEventListener(
    "click",
    sendMessage
);

// ===============================
// Enter Key
// ===============================

questionInput.addEventListener(
    "keydown",
    (event) => {

        if (event.key === "Enter") {

            event.preventDefault();

            sendMessage();

        }

    }
);

// ===============================
// Auto Focus
// ===============================

questionInput.focus();