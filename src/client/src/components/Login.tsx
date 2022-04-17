import Button from "react-bootstrap/Button";

export default function Login() {
    function handleClick() {
        console.log("The button was clicked");
    }

    return (
        <div>
            <p>You need to log in</p>
            <Button variant="secondary" onClick={handleClick}>This is a button</Button>
        </div>
    );
}