

function switchMode() {
    const tag = document.querySelector('link');
    //Needs to be 40 for light mode or 39 for dark
    if (tag.outerHTML.length === 40) {
        tag.setAttribute("href","dark.css");
    } else {
        tag.setAttribute("href","light.css");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const gameBoard = document.querySelector('.game-board');
    const playerPieces = document.querySelector('.player-pieces');
    const compPieces = document.querySelector('.comp-pieces');
    const pieces = document.querySelectorAll('.pieces');
    const pawn = document.querySelector('.pawn');
    const submarine = document.querySelector('.lancer');
    const silverGen = document.querySelector('.silver-general');
    const goldGen = document.querySelector('.gold-general');
    const jadeGeneral = document.querySelector('.jade-general');
    const king = document.querySelector('.king');
    const startButton = document.querySelector('#start');
    const turn = document.querySelector('#whose-go');
    const info = document.querySelector('#info');
    const gridBlocks = [];
    let horizontal = true;
    let gameEnd = false;
    let currentPlayer = "player";
    const width = 9;
  


    //Create Board
    function createBoard(boards, blocks) {
      for (let i = 0; i < width * width; i++) {
          const block = document.createElement("div");
          block.dataset.id = i;
          boards.appendChild(block);
          blocks.push(block);
      }
    }
    createBoard(gameBoard, gridBlocks)
  


    //pieces
    const pieceArr = [
      {
        name: "pawn",
        directions: [
            [0, 1],
            [0, width]
        ]
      },
      {
        name: "submarine",
        directions: [
            [0, 1, 2],
            [0, width, width*2]
        ]
      },
      {
        name: "silverGen",
        directions: [
            [0, 1, 2],
            [0, width, width*2]
        ]
      },
      {
        name: "goldGen",
        directions: [
            [0, 1, 2, 3],
            [0, width, width*2, width*3]
        ]
      },
      {
        name: "king",
        directions: [
            [0, 1, 2, 3, 4],
            [0, width, width*2, width*3, width*4]
        ]
      },
    ]
  


    //Draw the computers pieces in random locations
    function createPieces(piece) {
  
        const taken = current.some(index => compBlocks[randStart + index].classList.contains("taken"));
        const rightEdge = current.some(index => (randStart + index) % width === width - 1);
        const leftEdge = current.some(index => (randStart + index) % width === 0);
  
        if (!taken && !rightEdge && !leftEdge) current.forEach(index => compBlocks[randStart + index].classList.add("taken", piece.name));
  
        else createPieces(piece);
    }
    createPieces(pieceArr[0]);
    createPieces(pieceArr[1]);
    createPieces(pieceArr[2]);
    createPieces(pieceArr[3]);
    createPieces(pieceArr[4]);
  


    //Move around player piece
    pieces.forEach(piece => piece.addEventListener("drag", Drag));
    gridBlocks.forEach(block => block.addEventListener("drag", Drag));
    gridBlocks.forEach(block => block.addEventListener("dragover", dragOver));
    gridBlocks.forEach(block => block.addEventListener("dragenter", dragEnter));
    gridBlocks.forEach(block => block.addEventListener("leave", dragLeave));
    gridBlocks.forEach(block => block.addEventListener("drop", Drop));
    gridBlocks.forEach(block => block.addEventListener("dragend", dragEnd));
  
    let pieceNameIndex;
    let draggedPiece;
    let dragPieceMove;
  
    pieces.forEach(piece => piece.addEventListener("mousedown", (n) => {
      pieceNameIndex = n.target.id;
        console.log(pieceNameIndex);
    }))
  
    function Drag() {
        draggedPiece = this;
        dragPieceMove = this.childNodes.length;
        console.log(draggedPiece);
    }
  
    function dragOver(n) {
        n.preventDefault();
    }
  
    function dragEnter(n) {
        n.preventDefault();
    }
  
    function dragLeave() {
        console.log("drag leave");
    }
  
    function Drop() {
        let pieceNameLastID = draggedPiece.lastChild.id;
        let pieceClass = pieceNameLastID.slice(0, -2);
        console.log(pieceClass);
        let lastPieceIndex = parseInt(pieceNameLastID.substr(-1));
        let pieceLastID = lastPieceIndex + parseInt(this.dataset.id);
        console.log(pieceLastID);
  
        pieceIndex = parseInt(pieceNameIndex.substr(-1));
  
        pieceLastID = pieceLastID - pieceIndex;
        console.log(pieceLastID);
  
        if (horizontal && !newNAH.includes(pieceLastID)) {
            for (let i = 0; i < dragPieceMove; i++) {
                gridBlocks[parseInt(this.dataset.id) - pieceIndex + i].classList.add("taken", pieceClass);
            }
            //As long as the index of the piece you are dragging is not in the newNAV array. This means that sometimes if you drag the piece by its
            //index-1 , index-2 and so on, the piece will rebound back to the playerPieces.
        } else if (!horizontal && !newNAV.includes(pieceLastID)) {
            for (let i = 0; i < dragPieceMove; i++) {
                gridBlocks[parseInt(this.dataset.id) - pieceIndex + width * i].classList.add("taken", pieceClass);
            }
        } else return;
  
        playerPieces.removeChild(draggedPiece);
    }
  
    function dragEnd() {
        console.log("dragend");
    }
  


    //Game Logic
    function playGame() {
        if (gameEnd) return;
        if (currentPlayer === "player") {
            turn.innerHTML = "Your Go";
            compBlocks.forEach(block => block.addEventListener("click", function (n) {
                revealBlock(block)
            }));
        }
        if (currentPlayer === "computer") {
            turn.innerHTML = "Computers Go";
            setTimeout(compGo, 1000);
        }
    }
    startButton.addEventListener("click", playGame);
  
    let destroyerCount = 0;
    let submarineCount = 0;
    let cruiserCount = 0;
    let battleshipCount = 0;
    let carrierCount = 0;
  
    function revealBlock(block) {
        if (!block.classList.contains("boom")) {
            if (block.classList.contains("pawn")) destroyerCount++;
            if (block.classList.contains("submarine")) submarineCount++;
            if (block.classList.contains("silverGen")) cruiserCount++;
            if (block.classList.contains("goldGen")) battleshipCount++;
            if (block.classList.contains("king")) carrierCount++;
        }
        if (block.classList.contains("taken")) {
            block.classList.add("boom");
        } else {
            block.classList.add("miss");
        }
        checkWin();
        currentPlayer = "computer";
        playGame();
    }
  
    let cpuDestroyerCount = 0;
    let cpuSubmarineCount = 0;
    let cpuCruiserCount = 0;
    let cpuBattleshipCount = 0;
    let cpuCarrierCount = 0;
  
    function compGo() {
        let random = Math.floor(Math.random() * gridBlocks.length);
        if (!gridBlocks[random].classList.contains("boom")) {
            gridBlocks[random].classList.add("boom");
            if (gridBlocks[random].classList.contains("pawn")) cpuDestroyerCount++;
            if (gridBlocks[random].classList.contains("submarine")) cpuSubmarineCount++;
            if (gridBlocks[random].classList.contains("silverGen")) cpuCruiserCount++;
            if (gridBlocks[random].classList.contains("goldGen")) cpuBattleshipCount++;
            if (gridBlocks[random].classList.contains("king")) cpuCarrierCount++;
            checkWin();
        } else compGo();
        currentPlayer = "player";
        turn.innerHTML = "Your Turn";
    }

    function gameOver() {
        gameEnd = true;
        startButton.removeEventListener("click", playGame);
    }
  })