
import React from 'react';
import './statistic.css'

class Statitic extends React.Component {

  constructor(props) {
    super(props);
    this.state = {source: props.source, dest: props.source, totalElevation: props.totalElevation, distance: props.distance};
  }

  render() {
    return (
      <div className="container">
        <div className="info">Source: {this.state.source}</div>
        <div className="info">Destination: {this.state.dest}</div>
        <div className="info">Elevation: {this.state.elevation}</div>
        <div className="info">Distance: {this.state.distance}</div>
      </div>
    )
  }

}

export default Statitic;