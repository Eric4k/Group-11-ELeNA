import React from 'react';
import { MapContainer, TileLayer, useMap, Marker, Popup } from 'react-leaflet';
import Route from './route.js';
import L from "leaflet";
class Map extends React.Component {

  constructor(props) {
    super(props);
    this.coord = props.route.map(waypoint => L.latLng(waypoint.y, waypoint.x));
  }
  
  render() {
    return (
      <div>
        <MapContainer center={this.coord.length === 0 ? [42.3754, -72.5193] : this.coord[0]} zoom={13} scrollWheelZoom={true}>
          <Route coord={this.coord}/>
        </MapContainer>
      </div>

    );
  }


}

export default Map;