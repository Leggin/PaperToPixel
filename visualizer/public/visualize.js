import * as THREE from 'three';

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(
    75,                                      // Field of View
    window.innerWidth / window.innerHeight,  // aspect ratio
    0.1,                                     // near clipping plane
    1000                                     // far clipping plane
);
var renderer = new THREE.WebGLRenderer({
    alpha: true,     // transparent background
    antialias: true  // smooth edges
});

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

var geometry = new THREE.BoxGeometry(1, 1, 1);
var material = new THREE.MeshNormalMaterial();
var cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.z = 5; // move camera back so we can see the cube

var render = function() {
    requestAnimationFrame(render);
    renderer.render(scene, camera);

    // rotate cube a little each frame
    cube.rotation.x += 0.05;
    cube.rotation.y += 0.05;
};

render();