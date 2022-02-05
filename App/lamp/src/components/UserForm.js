import react from "react";

// TO CONVERT ALL INTO ARROW FUNCTIONS

/*
const UserForm = () => {
    return (
        <h1>Hello World</h1>
    );
}
*/

export class UserForm extends react.Component {
    constructor(props) {
        super(props);
        this.state = {
            nameValue: "",
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleReset = this.handleReset.bind(this);
        this.handleNameChange = this.handleNameChange.bind(this);
    }
    handleSubmit(event) {
        event.preventDefault();
        // Submit data
        this.setState({
            nameValue: "",
        });
    }
    handleReset(event) {
        this.setState({
            nameValue: "",
        });
    }
    handleNameChange(event) {
        this.setState({
            nameValue: event.target.value,
        });
    }
    render() {
        return(
            <div className="UserForm">
                <h2>Form</h2>
                <form onSubmit={this.handleSubmit} onReset={this.handleReset}>
                    <input 
                        type="text"
                        id="username"
                        name="username"
                        value={this.state.nameValue}
                        onChange={this.handleNameChange}
                        placeholder="Username"
                    />
                    <button type="submit">
                        Submit
                    </button>
                    <button type="reset">
                        Reset
                    </button>
                </form>
            </div>
        );
    }
}

export default UserForm;