const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");




let userMessage = null; 
const API_KEY = "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";
const inputInitHeight = chatInput.scrollHeight;

const createChatLi = (message, className) => {
    
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi; 
}

const generateResponse = (chatElement) => {
    const API_URL = "https://api.openai.com/v1/chat/completions";
    const messageElement = chatElement.querySelector("p");

    
    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{role: "user", content: userMessage}],
        })
    }

    
    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        messageElement.textContent = data.choices[0].message.content.trim();
    }).catch(() => {
        messageElement.classList.add("error");
        messageElement.textContent = "Oops! Something went wrong. Please try again.";
    }).finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
}

const handleChat = () => {
    userMessage = chatInput.value.trim(); 
    if(!userMessage) return;

    
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    
    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
    
    setTimeout(() => {
        const myStringArray = [
            "Still en route through the cosmic lag...",
            "Hitching a ride on the space-time delay express...",
            "Navigating the time-warp, almost there...",
            "Message en route, taking the scenic route through the cosmic lag...",
            "Incoming wisdom from the future, courtesy of cosmic lag...",
            "Signal cutting through the cosmic lag like a laser through fog...",
            "Transmission unfolding through the cosmic lag, like a slow-motion supernova...",
            "Cosmic lag? More like cosmic swag, as your message glides in gracefully...",
            "Patience, dear friend, as your words surf the celestial tides of the cosmic lag...",
            "Awaiting your words like an astronaut in stasis, traversing the cosmic lag...",
            "Your message is like a comet on a leisurely journey through the cosmic lag..."
        ];
        function chooseRandomString(stringsArray) {
            const randomIndex = Math.floor(Math.random() * stringsArray.length);
            return stringsArray[randomIndex];
        }
        const incomingChatLi = createChatLi(chooseRandomString(myStringArray), "incoming");
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(incomingChatLi);
    }, 600);
    
    
}

chatInput.addEventListener("input", () => {
    
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    
    if(e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendChatBtn.addEventListener("click", handleChat);
closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));