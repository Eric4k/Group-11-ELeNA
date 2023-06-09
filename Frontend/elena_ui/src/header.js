import React from 'react';
import './header.css';
import axios from 'axios';
import Map from './map';
import Statitic from './statistic';
import { v4 as uuidv4 } from 'uuid';
class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {source:"", dest:"", filterOpen: false, elevation: "min", transportation: "walk", algorithm: "dijkstra", deviation: 0, route: [], distance: "", totalElevation: "", loading: false};
    this.handleSearch = this.handleSearch.bind(this);
    this.handleFilter = this.handleFilter.bind(this);
    this.handleEvelation = this.handleEvelation.bind(this);
    this.handleTransportation = this.handleTransportation.bind(this);
    this.handleAlgorithm = this.handleAlgorithm.bind(this);
    this.handleDeviation = this.handleDeviation.bind(this);
  }
  
  //given a location and a source this function will call the api from the backend to return the route
  async handleSearch(event) {
    event.preventDefault();
    if (this.state.deviation > 100 || this.state.deviation < 0) {
      await this.setState({ deviation: 100 });
    }
    await this.setState({loading:true, source: document.getElementById('src1').value, dest: document.getElementById('dest1').value});
    
    const { data } = await axios.get('http://127.0.0.1:8000/route/get/', {
      params: {
        source: this.state.source,
        destination: this.state.dest,
        elev_preference: this.state.elevation,
        modeOfTransport: this.state.transportation,
        algorithm: this.state.algorithm,
        deviation: this.state.deviation,
      }
    });
    this.setState({loading:false});
    if (data !== undefined) {
      this.setState({route: data.route_detail.path, distance: parseInt(data.route_detail.route_length), totalElevation: parseInt(data.route_detail.net_elevation) });
    }
  }

  handleFilter(event) {
    this.setState((state) => {
      return {
        filterOpen: !state.filterOpen,
      }
    })
  }

  handleEvelation(event) {
    this.setState({elevation: event.target.name});
  }

  handleTransportation(event) {
    this.setState({transportation: event.target.name});
  }

  handleAlgorithm(event) {
    this.setState({algorithm: event.target.name});
  }

  handleDeviation(event) {
    this.setState({deviation: event.target.value})
  }

  render() {
    return (
      <div>
        <div className="header">
          <h1 className="logo">EleNa</h1>
          <div className="searchBox">
            <div className="searchInputContainer">
              <input type="text" placeholder="From..."  id="src1" className="inputText"/>
              <hr className="hr1"></hr>
              <input type="text" placeholder="To..."  id="dest1" className="inputText"/>
            </div>
            <input type="button" value="Search" onClick={this.handleSearch} className="searchBtn"/>
          </div>
          <input type="button" value="Filter" onClick={this.handleFilter} className="filterBtn"/>
        </div>
        {this.state.filterOpen && (
          //Dropdown that contains different options the user can filter by
          <div className="dropdown">
            <div className='options'>
              <input type="checkbox" name="min" className='optionBtn' checked={this.state.elevation === "min"} onChange={this.handleEvelation}></input><label> Min Elevation</label>
              <input type="checkbox" name="max" className='optionBtn' checked={this.state.elevation === "max"} onChange={this.handleEvelation}></input><label> Max Elevation</label>  
            </div>
            <hr className='hr2'></hr>
            <div className='options'> 
              <input type="checkbox" name="walk" className='optionBtn' checked={this.state.transportation === "walk"} onChange={this.handleTransportation}></input><label> Walk</label> 
              <input type="checkbox" name="bike" className='optionBtn' checked={this.state.transportation === "bike"} onChange={this.handleTransportation}></input><label> Bike</label>
            </div>
            <hr className='hr2'></hr>
            <div className='options'> 
              <input type="checkbox" name="dijkstra" className='optionBtn' checked={this.state.algorithm === "dijkstra"} onChange={this.handleAlgorithm}></input><label> Dijkstra</label>
              <input type="checkbox" name="astar" className='optionBtn' checked={this.state.algorithm === "astar"} onChange={this.handleAlgorithm}></input><label> A Star</label>  
            </div>
            <hr className='hr2'></hr>
            <div className='options'> 
              <label> % Deviation</label> <input type="number" value={this.deviation} className='optionBtn' onChange={this.handleDeviation} min="0" max="100"></input> 
            </div>
          </div>
        )}
       
        <Statitic key1={uuidv4()} key2={uuidv4()} key3={uuidv4()} key4={uuidv4()} source={this.state.source} dest={this.state.dest} distance={this.state.distance} totalElevation={this.state.totalElevation}/>
        {!this.state.loading && (
          //Given a route the Map compoenent will display it on a map utilizing leaflet
          <Map key={this.state.route} route={this.state.route} source={this.state.source} dest={this.state.dest} />
        )}
        {this.state.loading &&(       
          <div className='box'>
            <div className="ring">Loading
              <span className='spin'></span>
            </div>
          </div> 
        )}
      </div>
    )
  }
}

export default Header;