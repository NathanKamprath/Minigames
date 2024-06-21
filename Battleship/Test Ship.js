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
    const playerBoard = document.querySelector('.player-board');
    const compBoard = document.querySelector('.compuer-board');
    const shipDocks = document.querySelector('.dock');
    const ships = document.querySelectorAll('.ship');
    const patrol = document.querySelector('.patrol-prev');
    const submarine = document.querySelector('.submarine-prev');
    const destroyer = document.querySelector('.destroyer-prev');
    const battleship = document.querySelector('.battleship-prev');
    const carrier = document.querySelector('.carrier-prev');
    const startButton = document.querySelector('#start');
    const flipButton = document.querySelector('#flip');
    const turn = document.querySelector('#whose-go');
    const info = document.querySelector('#info');
    const playerBlocks = [];
    const compBlocks = [];
    let horizontal = true;
    let gameEnd = false;
    let currentPlayer = "player";
    const width = 10;
  


    //Create Board
    function createBoard(boards, blocks) {
      for (let i = 0; i < width * width; i++) {
          const block = document.createElement("div");
          block.dataset.id = i;
          boards.appendChild(block);
          blocks.push(block);
      }
    }
    createBoard(playerBoard, playerBlocks)
    createBoard(compBoard, compBlocks)
  


    //Ships
    const shipArr = [
      {
        name: "patrol",
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
        name: "destroyer",
        directions: [
            [0, 1, 2],
            [0, width, width*2]
        ]
      },
      {
        name: "battleship",
        directions: [
            [0, 1, 2, 3],
            [0, width, width*2, width*3]
        ]
      },
      {
        name: "carrier",
        directions: [
            [0, 1, 2, 3, 4],
            [0, width, width*2, width*3, width*4]
        ]
      },
    ]
  


    //Draw the computers ships in random locations
    function shipPiece(ship) {
        let randDir = Math.floor(Math.random() * ship.directions.length);
        let current = ship.directions[randDir];
        if (randDir === 0) direction = 1;
        if (randDir === 1) direction = 10;
        let randStart = Math.abs(Math.floor(Math.random() * compBlocks.length - (ship.directions[0].length * direction)));
  
        const taken = current.some(index => compBlocks[randStart + index].classList.contains("taken"));
        const rightEdge = current.some(index => (randStart + index) % width === width - 1);
        const leftEdge = current.some(index => (randStart + index) % width === 0);
  
        if (!taken && !rightEdge && !leftEdge) current.forEach(index => compBlocks[randStart + index].classList.add("taken", ship.name));
  
        else shipPiece(ship);
    }
    shipPiece(shipArr[0]);
    shipPiece(shipArr[1]);
    shipPiece(shipArr[2]);
    shipPiece(shipArr[3]);
    shipPiece(shipArr[4]);
  


    //Flip the ships
    function Flip() {
      if (horizontal) {
          patrol.classList.toggle("patrol-prev-vertical");
          submarine.classList.toggle("submarine-prev-vertical");
          destroyer.classList.toggle("destroyer-prev-vertical");
          battleship.classList.toggle("battleship-prev-vertical");
          carrier.classList.toggle("carrier-prev-vertical");
          horizontal = false;
          console.log(horizontal);
          return;
      };
      if (!horizontal) {
          patrol.classList.toggle("patrol-prev-vertical");
          submarine.classList.toggle("submarine-prev-vertical");
          destroyer.classList.toggle("destroyer-prev-vertical");
          battleship.classList.toggle("battleship-prev-vertical");
          carrier.classList.toggle("carrier-prev-vertical");
          horizontal = true;
          console.log(horizontal);
          return;
        };
    }
    flipButton.addEventListener("click", Flip);
  


    //Move around player ship
    ships.forEach(ship => ship.addEventListener("drag", Drag));
    playerBlocks.forEach(block => block.addEventListener("drag", Drag));
    playerBlocks.forEach(block => block.addEventListener("dragover", dragOver));
    playerBlocks.forEach(block => block.addEventListener("dragenter", dragEnter));
    playerBlocks.forEach(block => block.addEventListener("leave", dragLeave));
    playerBlocks.forEach(block => block.addEventListener("drop", Drop));
    playerBlocks.forEach(block => block.addEventListener("dragend", dragEnd));
  
    let shipNameIndex;
    let draggedShip;
    let dragShipLen;
  
    ships.forEach(ship => ship.addEventListener("mousedown", (n) => {
      shipNameIndex = n.target.id;
        console.log(shipNameIndex);
    }))
  
    function Drag() {
        draggedShip = this;
        dragShipLen = this.childNodes.length;
        console.log(draggedShip);
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
        let shipNameLastID = draggedShip.lastChild.id;
        let shipClass = shipNameLastID.slice(0, -2);
        console.log(shipClass);
        let lastShipIndex = parseInt(shipNameLastID.substr(-1));
        let shipLastID = lastShipIndex + parseInt(this.dataset.id);
        console.log(shipLastID);
        
        const notAllowedHorizontal = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 2, 22, 32, 42,
            52, 62, 72, 82, 92, 3, 13, 23, 33, 43, 53, 63, 73, 83, 93
        ];
        const notAllowedVertical = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76,
            75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60
        ];
        let newNAH = notAllowedHorizontal.splice(0, 10 * lastShipIndex);
        let newNAV = notAllowedVertical.splice(0, 10 * lastShipIndex);
  
        shipIndex = parseInt(shipNameIndex.substr(-1));
  
        shipLastID = shipLastID - shipIndex;
        console.log(shipLastID);
  
        if (horizontal && !newNAH.includes(shipLastID)) {
            for (let i = 0; i < dragShipLen; i++) {
                playerBlocks[parseInt(this.dataset.id) - shipIndex + i].classList.add("taken", shipClass);
            }
            //As long as the index of the ship you are dragging is not in the newNAV array. This means that sometimes if you drag the ship by its
            //index-1 , index-2 and so on, the ship will rebound back to the shipDocks.
        } else if (!horizontal && !newNAV.includes(shipLastID)) {
            for (let i = 0; i < dragShipLen; i++) {
                playerBlocks[parseInt(this.dataset.id) - shipIndex + width * i].classList.add("taken", shipClass);
            }
        } else return;
  
        shipDocks.removeChild(draggedShip);
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
            if (block.classList.contains("patrol")) destroyerCount++;
            if (block.classList.contains("submarine")) submarineCount++;
            if (block.classList.contains("destroyer")) cruiserCount++;
            if (block.classList.contains("battleship")) battleshipCount++;
            if (block.classList.contains("carrier")) carrierCount++;
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
        let random = Math.floor(Math.random() * playerBlocks.length);
        if (!playerBlocks[random].classList.contains("boom")) {
            playerBlocks[random].classList.add("boom");
            if (playerBlocks[random].classList.contains("patrol")) cpuDestroyerCount++;
            if (playerBlocks[random].classList.contains("submarine")) cpuSubmarineCount++;
            if (playerBlocks[random].classList.contains("destroyer")) cpuCruiserCount++;
            if (playerBlocks[random].classList.contains("battleship")) cpuBattleshipCount++;
            if (playerBlocks[random].classList.contains("carrier")) cpuCarrierCount++;
            checkWin();
        } else compGo();
        currentPlayer = "player";
        turn.innerHTML = "Your Turn";
    }
  


    //Game End
    function checkWin() {
      if (destroyerCount === 2) {
          info.innerHTML = "You sunk the computers patroler";
          destroyerCount = 10;
      }
      if (submarineCount === 3) {
          info.innerHTML = "You sunk the computers submarine";
          submarineCount = 10;
      }
      if (cruiserCount === 3) {
          info.innerHTML = "You sunk the computers destroyer";
          cruiserCount = 10;
      }
      if (battleshipCount === 4) {
          info.innerHTML = "You sunk the computers battleship";
          battleshipCount = 10;
      }
      if (carrierCount === 5) {
          info.innerHTML = "You sunk the computers carrier";
          carrierCount = 10;
      }
      if (cpuDestroyerCount === 2) {
          info.innerHTML = "You sunk the computers patrol";
          cpuDestroyerCount = 10;
      }
      if (cpuSubmarineCount === 3) {
          info.innerHTML = "You sunk the computers Submarine";
          cpuSubmarineCount = 10;
      }
      if (cpuCruiserCount === 3) {
          info.innerHTML = "You sunk the computers destroyer";
          cpuCruiserCount = 10;
      }
      if (cpuBattleshipCount === 4) {
          info.innerHTML = "You sunk the computers Battleship";
          cpuBattleshipCount = 10;
      }
      if (cpuCarrierCount === 5) {
          info.innerHTML = "You sunk the computers Carrier";
          cpuCarrierCount = 10;
      }
      if ((destroyerCount + submarineCount + cruiserCount + battleshipCount + carrierCount) === 50) {
          info.innerHTML = "YOU WIN";
          gameOver();
      }
      if ((cpuDestroyerCount + cpuSubmarineCount + cpuCruiserCount + cpuBattleshipCount + cpuCarrierCount) === 50) {
          info.innerHTML = "COMPUTER WINS";
          gameOver();
      }
    }
  
    function gameOver() {
        gameEnd = true;
        startButton.removeEventListener("click", playGame);
    }
  })