import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();


// TODO: figure out how to properly integrate mpabox
// document.head.appendChild("<link href='https://api.mapbox.com/mapbox-gl-js/v1.4.1/mapbox-gl.css' rel='stylesheet' />");

// var mapboxgl = require('mapbox-gl/dist/mapbox-gl.js');
 
// mapboxgl.accessToken = 'pk.eyJ1IjoicG1pZWxuaWsiLCJhIjoiY2sxbXczdGRlMDB1aTNkcG1vdGNjZ2xtZyJ9.mI1uYWstyLnh8yZN0GrbUw';
// var map = new mapboxgl.Map({
// container: 'HomePage',     //TODO: Replace 'YOUR_CONTAINER_ELEMENT_ID' with the id of an element on your page where you would like your map.
// style: 'mapbox://styles/mapbox/streets-v11'
// });
