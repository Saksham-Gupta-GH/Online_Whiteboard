let canvas = document.getElementById("board");
let ctx = canvas.getContext("2d");
let mode = "draw";
let drawing = false;
let notes = [];
let drawings = [];

canvas.addEventListener("mousedown", e => {
    if (mode === "draw") {
        drawing = true;
        ctx.beginPath();
        ctx.moveTo(e.offsetX, e.offsetY);
    } else if (mode === "note") {
        let text = prompt("Enter note text:");
        if (text) {
            notes.push({ x: e.offsetX, y: e.offsetY, text });
            drawAll();
        }
    }
});

canvas.addEventListener("mousemove", e => {
    if (drawing && mode === "draw") {
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
        drawings.push({ x: e.offsetX, y: e.offsetY });
    }
});

canvas.addEventListener("mouseup", () => {
    drawing = false;
});

function setMode(m) {
    mode = m;
}

function drawAll() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Redraw drawings
    ctx.beginPath();
    for (let i = 0; i < drawings.length; i++) {
        let p = drawings[i];
        ctx.lineTo(p.x, p.y);
    }
    ctx.stroke();

    // Redraw notes
    ctx.fillStyle = "yellow";
    notes.forEach(note => {
        ctx.fillRect(note.x, note.y, 100, 50);
        ctx.fillStyle = "black";
        ctx.fillText(note.text, note.x + 5, note.y + 25);
        ctx.fillStyle = "yellow";
    });
}

async function saveBoard() {
    let name = prompt("Enter board name:");
    if (!name) return;

    let data = { drawings, notes };
    await fetch("/save", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, data })
    });

    alert("Board saved!");
    fetchBoards();
}

async function fetchBoards() {
    let res = await fetch("/load");
    let boards = await res.json();
    let select = document.getElementById("boardList");
    select.innerHTML = "";
    boards.forEach(b => {
        let opt = document.createElement("option");
        opt.value = b.id;
        opt.innerText = b.name;
        select.appendChild(opt);
    });
}

async function loadBoard() {
    let id = document.getElementById("boardList").value;
    if (!id) return;
    let res = await fetch("/load/" + id);
    let data = await res.json();

    drawings = data.drawings || [];
    notes = data.notes || [];
    drawAll();
}

fetchBoards();
