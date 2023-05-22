import React from 'react';
import { MapContainer, TileLayer, useMap, Marker, Popup } from 'react-leaflet';
import Route from './route.js';
import L from "leaflet";
import './map.css'
import { PureComponent } from 'react';
class Map extends PureComponent {

  constructor(props) {
    super(props);
    this.coord = props.route.map(waypoint => L.latLng(waypoint.y, waypoint.x));
    this.source = props.source;
    this.dest = props.dest;
  }
  
  render() {
    return (
        <MapContainer center={this.coord.length === 0 ? [42.3754, -72.5193] : this.coord[0]} zoom={13} scrollWheelZoom={true}>
          <Route coord={this.coord} source={this.source} dest={this.dest}/>
        </MapContainer>
    );
  }
}

export default Map;