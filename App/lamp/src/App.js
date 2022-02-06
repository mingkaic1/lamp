import react from 'react';
import UserForm from './components/UserForm.js'

export class App extends react.Component {
  handleSubmitUserForm(inputValues) {
    console.log(inputValues);
  }
  render() {
    return (
      <div className="App">
        <UserForm onSubmit={this.handleSubmitUserForm}/>
      </div>
    );
  }
}

export default App;
