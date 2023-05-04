// Gerando Token
(async function func(){
    console.clear();
    const headers = {
        'Content-Type': 'application/json',
    };
    const body = JSON.stringify({
        "username": "login",
        "password": "senha"
        
    });
    const config = {
        method: 'POST',
        headers: headers,
        body: body
    };

    const response = await fetch(
        'http://127.0.0.1:8000/recipes/api/token/',
        config
    );

    const json = await response.json();
    
    console.log('STATUS', response.status);
    console.log(json.access);

})();

// Autenticando 
(async function func(){
    console.clear();
    const headers = {
        authorization: 'Bearer token---'
    };
    const config = {
        method: 'GET',
        headers: headers,
    };

    const response = await fetch(
        'http://127.0.0.1:8000/authors/api/me/',
        config
    );

    const json = await response.json();
    
    console.log('STATUS', response.status);
    console.log(json);

})();