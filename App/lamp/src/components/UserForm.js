import react from "react";

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
                </form>
            </div>
        );
    }
}

export default UserForm;