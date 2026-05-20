document.addEventListener('DOMContentLoaded', async () => {
    const res = await fetch('/list');
    const data = await res.json();
    
    console.log(data);

    const result = document.getElementById('card-list');
    data.forEach(post => {
        makeCard(post.id, post.title, post.message);
    })
});

document.getElementById('card-list').addEventListener('click', async (e) => {
    console.log(e.target);
});

function makeCard(id, title, message) {
    const card = document.createElement('div');
    card.innerHTML = `
    <div>
        <p>${id}</p>
        <p>${title}</p>
        <p>${message}</p>
        <button>Modify</button>
        <button>Delete</button>
    </div>
    `
    document.getElementById('card-list').appendChild(card);
}

document.getElementById('input-submit-btn').addEventListener('click', () => {
    const title = document.getElementById('input-title').value;
    const content = document.getElementById('input-text').value;
    
    fetch('/create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify({title, content}),
    })
    .then(response => response.json())
    .then(data => console.log('[CREATE] success:', data))
    .catch(error => console.error('[CREATE] failed:', error));
});