import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        {/* <img
          src="../../public/favicon.png"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        /> */}
        <img src={require('../public/favicon.png')} />
        <hr />
        <h1>React + Django Rest Api Crud Tesing</h1>
      </div>
    );
  }
}

export default Header;
