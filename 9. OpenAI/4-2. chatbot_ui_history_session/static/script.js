// 1. DOM이 로딩 된 다음에 호출
document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.getElementById('user-input');
    const formInput = document.getElementById('user-input-form');
    const resultDiv = document.getElementById('result');
    const newChatBtn = document.getElementById('new-chat-btn');
    const allChatBtn = document.getElementById('all-chat-btn');

    newChatBtn.addEventListener('click', async () => {
        res = await fetch('/api/refresh');
        resultDiv.innerHTML='';
    });

    allChatBtn.addEventListener('click', async () => {
        // 한 번만 되게끔 해야함
        res = await fetch('/api/chat-all');
        data = await res.json();

        for (let i = 0; i < data.length; i++)
            appendMessage(data[i]['content'], data[i]['role']);
    });

    formInput.addEventListener('submit', async (e) => {
        e.preventDefault();

        const chatMsg = chatInput.value.trim();
        if (!chatMsg) return; 

        appendMessage(chatMsg, 'user');
        chatInput.value = '';
        scrollToBottom();

        try {
            const replyData = await fetchChatReply(chatMsg);
            
            appendMessage(replyData.reply, 'system');
            scrollToBottom();
        } catch (error) {
            console.error('통신 에러:', error);
            appendMessage('메시지를 보내는데 실패했습니다.', 'system');
        }
    });

    async function fetchChatReply(message) {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ chatMsg: message })
        });
        
        if (!res.ok) throw new Error('Network response was not ok');
        return await res.json();
    }

    /**
    * @param {string} text - 메시지 내용
    * @param {'user' | 'system'} sender - 보낸 사람 구분
    **/
    function appendMessage(text, sender) {
        // CSS (.message, .user, .system)와 매칭되도록 div로 생성
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        messageDiv.innerText = text;
        
        resultDiv.appendChild(messageDiv);
    }

    function scrollToBottom() {
        resultDiv.scrollTop = resultDiv.scrollHeight;
    }
});