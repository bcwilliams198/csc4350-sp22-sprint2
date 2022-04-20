// IMPORTS
// third-party
import Button from "react-bootstrap/Button";

export default function Login() {
    async function handleClick() {
        const response = await fetch("/login_request", {mode: 'no-cors'});
        const google_url = await response.json();
        window.location.href = google_url;
    }

    return (
        <div>
            <p>You need to log in</p>
            <Button variant="secondary" onClick={handleClick}>This is a button</Button>
        </div>
    );
}