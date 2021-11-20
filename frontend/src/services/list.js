export default function getList() {
    return fetch('http://localhost:8000')
        .then(data => data.json())
}