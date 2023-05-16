import React from 'react';
import { MapContainer, TileLayer, useMap, Marker, Popup } from 'react-leaflet';
import Route from './route.js';
import L from "leaflet";
class Map extends React.Component {

  constructor(props) {
    super(props);
    this.coord = props.route.map(waypoint => L.latLng(waypoint.y, waypoint.x));
//     this.coord = [
//       {
//           "y": 42.394595,
//           "x": -72.523556,
//           "street_count": 2,
//           "elevation": 88.0
//       },
//       {
//           "y": 42.394668,
//           "x": -72.523567,
//           "street_count": 2,
//           "elevation": 87.0
//       },
//       {
//           "y": 42.394741,
//           "x": -72.523578,
//           "street_count": 2,
//           "elevation": 85.0
//       },
//       {
//           "y": 42.394808,
//           "x": -72.523585,
//           "street_count": 2,
//           "elevation": 85.0
//       },
//       {
//           "y": 42.394876,
//           "x": -72.523591,
//           "street_count": 2,
//           "elevation": 85.0
//       },
//       {
//           "y": 42.394944,
//           "x": -72.5236,
//           "street_count": 2,
//           "elevation": 84.0
//       },
//       {
//           "y": 42.395019,
//           "x": -72.523611,
//           "street_count": 2,
//           "elevation": 84.0
//       },
//       {
//           "y": 42.395094,
//           "x": -72.523626,
//           "street_count": 2,
//           "elevation": 83.0
//       },
//       {
//           "y": 42.395166,
//           "x": -72.523653,
//           "street_count": 2,
//           "elevation": 82.0
//       },
//       {
//           "y": 42.39521,
//           "x": -72.523676,
//           "street_count": 2,
//           "elevation": 81.0
//       },
//       {
//           "y": 42.395252,
//           "x": -72.523704,
//           "street_count": 2,
//           "elevation": 81.0
//       },
//       {
//           "y": 42.395292,
//           "x": -72.523736,
//           "street_count": 2,
//           "elevation": 80.0
//       },
//       {
//           "y": 42.395332,
//           "x": -72.523777,
//           "street_count": 2,
//           "elevation": 79.0
//       },
//       {
//           "y": 42.39537,
//           "x": -72.523823,
//           "street_count": 2,
//           "elevation": 78.0
//       },
//       {
//           "y": 42.395407,
//           "x": -72.523869,
//           "street_count": 2,
//           "elevation": 77.0
//       },
//       {
//           "y": 42.395463,
//           "x": -72.523928,
//           "street_count": 2,
//           "elevation": 75.0
//       },
//       {
//           "y": 42.395519,
//           "x": -72.523987,
//           "street_count": 2,
//           "elevation": 74.0
//       },
//       {
//           "y": 42.3955579,
//           "x": -72.5240344,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.395574,
//           "x": -72.524049,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.395624,
//           "x": -72.524116,
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.395674,
//           "x": -72.524186,
//           "street_count": 2,
//           "elevation": 69.0
//       },
//       {
//           "y": 42.395724,
//           "x": -72.524254,
//           "street_count": 2,
//           "elevation": 69.0
//       },
//       {
//           "y": 42.395771,
//           "x": -72.524307,
//           "street_count": 2,
//           "elevation": 69.0
//       },
//       {
//           "y": 42.395818,
//           "x": -72.524358,
//           "street_count": 2,
//           "elevation": 69.0
//       },
//       {
//           "y": 42.395866,
//           "x": -72.524408,
//           "street_count": 2,
//           "elevation": 69.0
//       },
//       {
//           "y": 42.395901,
//           "x": -72.524442,
//           "street_count": 2,
//           "elevation": 69.0
//       },
//       {
//           "y": 42.395936,
//           "x": -72.524475,
//           "street_count": 2,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.395977,
//           "x": -72.5245117,
//           "street_count": 3,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3958735,
//           "x": -72.5248365,
//           "highway": "crossing",
//           "street_count": 2,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3958069,
//           "x": -72.5250186,
//           "street_count": 3,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3958838,
//           "x": -72.5250673,
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.3960765,
//           "x": -72.5251798,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.3963304,
//           "x": -72.5253185,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.3964704,
//           "x": -72.5254023,
//           "street_count": 3,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.3965034,
//           "x": -72.5253614,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.3965479,
//           "x": -72.5253235,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.3966269,
//           "x": -72.5253079,
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.3967043,
//           "x": -72.5253458,
//           "street_count": 2,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3967619,
//           "x": -72.5254506,
//           "street_count": 2,
//           "elevation": 69.0
//       },
//       {
//           "y": 42.3967848,
//           "x": -72.5255548,
//           "street_count": 4,
//           "elevation": 68.0
//       },
//       {
//           "y": 42.3966994,
//           "x": -72.5258207,
//           "street_count": 2,
//           "elevation": 68.0
//       },
//       {
//           "y": 42.3965396,
//           "x": -72.5263291,
//           "street_count": 2,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3963829,
//           "x": -72.5268272,
//           "street_count": 4,
//           "elevation": 68.0
//       },
//       {
//           "y": 42.3963262,
//           "x": -72.5270073,
//           "street_count": 3,
//           "elevation": 69.0
//       },
//       {
//           "y": 42.3961845,
//           "x": -72.5269264,
//           "street_count": 2,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3956577,
//           "x": -72.5266256,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.3957157,
//           "x": -72.5264391,
//           "street_count": 3,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.3956874,
//           "x": -72.5264231,
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.3954964,
//           "x": -72.5263047,
//           "highway": "crossing",
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.395418,
//           "x": -72.526229,
//           "street_count": 4,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3953658,
//           "x": -72.5264051,
//           "street_count": 3,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.3953306,
//           "x": -72.5266042,
//           "highway": "crossing",
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.3953208,
//           "x": -72.5266752,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.395327,
//           "x": -72.5267553,
//           "street_count": 2,
//           "elevation": 74.0
//       },
//       {
//           "y": 42.3953376,
//           "x": -72.5268163,
//           "street_count": 3,
//           "elevation": 74.0
//       },
//       {
//           "y": 42.3953515,
//           "x": -72.5268485,
//           "street_count": 3,
//           "elevation": 74.0
//       },
//       {
//           "y": 42.3953624,
//           "x": -72.5268956,
//           "street_count": 2,
//           "elevation": 75.0
//       },
//       {
//           "y": 42.395364,
//           "x": -72.5269449,
//           "street_count": 2,
//           "elevation": 75.0
//       },
//       {
//           "y": 42.3953562,
//           "x": -72.5269932,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3953396,
//           "x": -72.5270371,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3953152,
//           "x": -72.5270738,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3952846,
//           "x": -72.5271008,
//           "street_count": 3,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3952655,
//           "x": -72.5271111,
//           "street_count": 3,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3952209,
//           "x": -72.5271198,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3951764,
//           "x": -72.5271091,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3951368,
//           "x": -72.5270799,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.395106,
//           "x": -72.5270352,
//           "street_count": 3,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3950966,
//           "x": -72.5270134,
//           "street_count": 3,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3950294,
//           "x": -72.5269638,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3949579,
//           "x": -72.526903,
//           "highway": "crossing",
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3948838,
//           "x": -72.526813,
//           "street_count": 3,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3946691,
//           "x": -72.5266848,
//           "street_count": 2,
//           "elevation": 79.0
//       },
//       {
//           "y": 42.3944193,
//           "x": -72.526539,
//           "street_count": 2,
//           "elevation": 80.0
//       },
//       {
//           "y": 42.3942982,
//           "x": -72.5264681,
//           "street_count": 2,
//           "elevation": 78.0
//       },
//       {
//           "y": 42.3940456,
//           "x": -72.5263202,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3939275,
//           "x": -72.5262564,
//           "street_count": 2,
//           "elevation": 76.0
//       },
//       {
//           "y": 42.3938026,
//           "x": -72.5261693,
//           "street_count": 2,
//           "elevation": 75.0
//       },
//       {
//           "y": 42.393516,
//           "x": -72.526006,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.393481,
//           "x": -72.525985,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.393447,
//           "x": -72.525963,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.393412,
//           "x": -72.525943,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.393386,
//           "x": -72.5259278,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.393371,
//           "x": -72.525919,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.393331,
//           "x": -72.525897,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.39329,
//           "x": -72.525875,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.393189,
//           "x": -72.525827,
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.393079,
//           "x": -72.5257888,
//           "highway": "crossing",
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.3929374,
//           "x": -72.5257373,
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.392777,
//           "x": -72.5256814,
//           "street_count": 3,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.3926474,
//           "x": -72.5256364,
//           "highway": "crossing",
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.3925804,
//           "x": -72.5256131,
//           "street_count": 3,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.3925689,
//           "x": -72.5256909,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.3925649,
//           "x": -72.5258269,
//           "street_count": 2,
//           "elevation": 71.0
//       },
//       {
//           "y": 42.392515,
//           "x": -72.5260635,
//           "street_count": 2,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3925092,
//           "x": -72.5260995,
//           "street_count": 2,
//           "elevation": 70.0
//       },
//       {
//           "y": 42.3924506,
//           "x": -72.5263352,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.3924303,
//           "x": -72.5263717,
//           "street_count": 2,
//           "elevation": 72.0
//       },
//       {
//           "y": 42.3923988,
//           "x": -72.5263704,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.3923605,
//           "x": -72.5263689,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.3921487,
//           "x": -72.5262022,
//           "street_count": 2,
//           "elevation": 73.0
//       },
//       {
//           "y": 42.3918866,
//           "x": -72.5261382,
//           "street_count": 2,
//           "elevation": 68.0
//       },
//       {
//           "y": 42.3918517,
//           "x": -72.526127,
//           "street_count": 2,
//           "elevation": 67.0
//       },
//       {
//           "y": 42.3916494,
//           "x": -72.5260623,
//           "street_count": 2,
//           "elevation": 64.0
//       },
//       {
//           "y": 42.3916141,
//           "x": -72.5260089,
//           "street_count": 2,
//           "elevation": 65.0
//       },
//       {
//           "y": 42.3911651,
//           "x": -72.5259201,
//           "street_count": 1,
//           "elevation": 67.0
//       }
//   ].map(waypoint => L.latLng(waypoint.y, waypoint.x));
    
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