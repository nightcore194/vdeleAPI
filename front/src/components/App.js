import React, { Component } from 'react';
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/vmain")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <ul>
        {this.state.data.map(User => {
          return (
            <li key={User.id}>
              {User.user_name} - {User.user_email}
            </li>
          );
        })}
      </ul>
    );
    return (
        <ul>
        {this.state.data.map(UserData => {
          return (
            <li key={UserData.id}>
              {UserData.user_social_vk} - {UserData.user_social_inst}
            </li>
          );
        })}
      </ul>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);