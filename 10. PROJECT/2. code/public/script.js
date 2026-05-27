document.getElementById('container').addEventListener('submit', async (e) => {
    e.preventDefault();

    const code_link = document.getElementById('code_link');

    const res = await fetch('/api/code_linkcheck', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code_link: code_link.value })
    });
    const data = await res.json();
    appendCodeMsg(data.code);
    appendResultMsg(data.result);
});

function appendResultMsg(msg) {
    const result = document.getElementById('result');
    result.innerHTML = marked.parse(msg);
    result.scrollTop = result.scrollHeight;
}

function appendCodeMsg(msg) {
    const code = document.getElementById('code');
    code.innerHTML = msg;
    code.scrollTop = code.scrollHeight;
}