document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chatform');
    
    if (chatForm) {            
        chatForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            const inputArea = document.getElementById('userInput');
            const messageText = inputArea.value.trim();
            
            if (messageText === '') return;

            appendMessage('user', messageText);
            inputArea.value = '';
            
            const res = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: messageText, baseURI: chatForm.baseURI })
            });

            const reader = res.body.getReader();
            const decoder = new TextDecoder();
            const botMessageContentDiv = appendMessage('bot', '');

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                const chunk = decoder.decode(value);
                const lines = chunk.split('\n');

                for (const line of lines) {
                    if (line.startsWith('data: ')) {
                        const data = line.slice(6);

                        if (data === '[DONE]') continue;

                        try {
                            const parsed = JSON.parse(data);

                            if (parsed.content) {
                                botMessageContentDiv.innerText += parsed.content;

                                const chatBox = document.getElementById('chatBox');
                                if (chatBox) {
                                    chatBox.scrollTop = chatBox.scrollHeight;
                                }
                                await new Promise(resolve => requestAnimationFrame(resolve));
                            }

                        } catch (e) {
                            console.log('JSON 파싱 에러:', e);
                        }
                    }
                }
            }
        });
    }
});

function appendMessage(sender, text) {
    const chatBox = document.getElementById('chatBox');
    if (!chatBox) return null;
    
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);

    if (sender === 'bot') {
        messageDiv.innerHTML = `
            <div class="avatar">🤖</div>
            <div class="message-content">${text}</div>
        `;
    } else {
        messageDiv.innerHTML = `
            <div class="message-content">${text}</div>
        `;
    }
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; 
    
    return messageDiv.querySelector('.message-content');
}