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
            inputValues: {
                username: "",
                email: "",
            }
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleReset = this.handleReset.bind(this);
        this.handleNameChange = this.handleNameChange.bind(this);
        this.handleEmailChange = this.handleEmailChange.bind(this);
    }
    handleSubmit(event) {
        event.preventDefault();
        this.props.onSubmit(this.state.inputValues);
        this.resetFields();
    }
    handleReset(event) {
        this.resetFields();
    }
    resetFields() {
        this.setState({
            inputValues: {
                username: "",
                email: "",
            }
        });
    }
    handleNameChange(event) {
        const inputValuesTemp = this.state.inputValues;
        inputValuesTemp.username = event.target.value;
        this.setState({
            inputValues: inputValuesTemp,
        });
    }
    handleEmailChange(event) {
        const inputValuesTemp = this.state.inputValues;
        inputValuesTemp.email = event.target.value;
        this.setState({
            inputValues: inputValuesTemp,
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
                        value={this.state.inputValues.username}
                        onChange={this.handleNameChange}
                        placeholder="Username"
                    />
                    <input 
                        type="text"
                        id="email"
                        name="email"
                        value={this.state.inputValues.email}
                        onChange={this.handleEmailChange}
                        placeholder="Email"
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