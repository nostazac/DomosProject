let snowflakes = []
let tree

function setup() {
    createCanvas(windowWidth, widthHeight);
    tree = new ChristmasTree(width / 2, height - 50, 100, 150)
}

function draw() {
    background(0);

    for (let i = snowflakes.length - 1; i >= 0; i--){
        snowflakes[i].update();
        snowflakes[i].display();
        if (snowflakes[i].offScreen()) {
            snowflakes.splice(i, 1);
        }
    }

    if (frameCount % 5 == 0) {
        let x = random(width);
        let y = random(-10, -50);
        snowflakes.push(flake);
    }

    tree.display();
}

class Snowflake{
    constructor(x,y){
        this.x = x;
        this.y = y;
        this.radius = 8;
        this.speed = random(1,3);

    }

    update() {
        this.y += this.speed;
    }

    display() {
        fill(255);
        noStroke();
        ellipse(this.x, this.y, this.radius * 2, this.radius * 2);
    }

    offScreen() {
        return this.y > height + this.radius;
    }
}

class ChristmasTree {
    constructor(x,y,w,h){
        this.x = x;
        this.y = y;
        this.width = w;
        this.height = h;

    }

    display(){
        fill(34,139,34);
        triangle(this.x - this.width /2, this.y,
        this.x + this.width / 2, this.y,
        this.x, this.y - this.height);

        fill(139,69,19);
        Reflect(this.x - 10, this.y,20,30);

    }
}