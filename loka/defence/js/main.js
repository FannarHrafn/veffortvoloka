/**
 * Generated from the Phaser Sandbox
 *
 * //phaser.io/sandbox/MAwBfzGW
 *
 * This source requires Phaser 2.6.2
 */

var game = new Phaser.Game(800, 600, Phaser.AUTO, '', { preload: preload, create: create, update: update, render: render });

function preload() {

    game.load.baseURL = 'http://examples.phaser.io/assets/';
    game.load.crossOrigin = 'anonymous';

    game.load.image('phaser', 'sprites/healthbar.png');
    game.load.image('ball', 'sprites/pangball.png');

}
var image;

var circle
var sprite
var radius = 150
var cX
var cY
var angle = 0
var speed=5

var leftKey, rightKey

function create() {
    //physics
    game.physics.startSystem(Phaser.Physics.ARCADE);
    //sprites
    ball = game.add.sprite(400, 200, 'ball');
    sprite = game.add.sprite(0, 0, 'phaser');
    sprite.anchor.set(0.5)
    //bæti við physics við sprites
    game.physics.enable([sprite,ball], Phaser.Physics.ARCADE)
    //geri varnarsprite immovable svo hann skoppar ekki í burt þegar hann ver
    sprite.body.immovable = true;
    //hraði á bolta
    ball.body.velocity.setTo(500, 500);
    //skoppar af  skjánum
    ball.body.collideWorldBounds = true;
    //heldur allri orku þegar  hann skoppar
    ball.body.bounce.setTo(1, 1);
    
    game.forceSingleUpdate=true
    
    cX = game.world.centerX
    cY = game.world.centerY

    circle = game.add.graphics()    
    circle.lineStyle(2,0xFF0000)
    circle.drawCircle(cX,cY,radius*2)
    
    
    // give it an initial position
   moveSpriteOnCircle(angle)
   
   leftKey = game.input.keyboard.addKey(Phaser.Keyboard.LEFT);
   rightKey = game.input.keyboard.addKey(Phaser.Keyboard.RIGHT);

   
}


function moveSpriteOnCircle(deg) {
    
    var theta = Phaser.Math.degToRad(deg)
    
    var newX = Math.sin(theta) * radius;
    var newY = Math.cos(theta) * radius;
    
    sprite.x=cX - newX;
    sprite.y=cY - newY;
    
}

function update() {

    var moved=false
    //varnarsprite og bolti skoppa af hvor öðrum
    game.physics.arcade.collide(sprite, ball);
    //sprite.angle svo hann snúist meðfram hringnum
    if(leftKey.isDown) {
        angle+=speed
        moved=true
        sprite.angle-=5
    }
    
    if(rightKey.isDown) {
        angle-=speed
        moved=true
        sprite.angle+=5
    }
    
    if(angle>=360) 
    {
        angle=360-angle
    }
    
    if(moved) {
        moveSpriteOnCircle(angle)
    }
}

function render() {

}
