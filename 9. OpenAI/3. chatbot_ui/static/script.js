// 1. DOM이 로딩 된 다음에 호출
document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.getElementById('user-input');
    const formInput = document.getElementById('user-input-form');
    const resultDiv = document.getElementById('result');

    formInput.addEventListener('submit', async (e) => {
        e.preventDefault();

        const chatMsg = chatInput.value.trim();
        if (!chatMsg) return; 

        // 1. 사용자가 입력한 메시지를 화면에 먼저 띄우기
        appendMessage(chatMsg, 'user');
        chatInput.value = ''; // 입력창 비우기
        scrollToBottom();

        try {
            // 2. API 서브루틴 호출 (Fetch 분리)
            const replyData = await fetchChatReply(chatMsg);
            
            // 3. 챗봇 응답을 화면에 띄우기
            appendMessage(replyData.reply, 'bot');
            scrollToBottom();
        } catch (error) {
            console.error('통신 에러:', error);
            appendMessage('메시지를 보내는데 실패했습니다.', 'bot');
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
    * @param {'user' | 'bot'} sender - 보낸 사람 구분
    **/
    function appendMessage(text, sender) {
        // CSS (.message, .user, .bot)와 매칭되도록 div로 생성
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        messageDiv.innerText = text;
        
        resultDiv.appendChild(messageDiv);
    }

    function scrollToBottom() {
        resultDiv.scrollTop = resultDiv.scrollHeight;
    }
});