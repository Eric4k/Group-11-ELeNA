
import React from 'react';
import './statistic.css'

class Statitic extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="container">
        <div key={this.props.key1} className="info">Source: {this.props.source}</div>
        <div key={this.props.key2} className="info">Destination: {this.props.dest}</div>
        <div key={this.props.key3} className="info">Elevation: {this.props.totalElevation}</div>
        <div key={this.props.key4} className="info">Distance: {this.props.distance}</div>
      </div>
    )
  }

}

export default Statitic;