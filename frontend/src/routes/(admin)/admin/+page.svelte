<script>
    import '$src/app.css'
    let username = '';
    let password = '';
    let loginFail = '';
    let token = '';
  
    async function login() {
        const response = await fetch('/admin', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const result = await response.json();

        if (result.success) {
            localStorage.setItem("jwt_token", result.token);
            localStorage.setItem("refresh_token", result.refresh);
            localStorage.setItem("username", result.username);
            localStorage.setItem("role", result.role);
            window.location.href = '/admin/home';
        } else {
            if (result.message != "Invalid credentials") {
                 loginFail = "Error: No database connection";
            }
            else { 
                loginFail = "Error: " + result.message;
            }
        }
    }
</script>
  
<title>Admin | Train Station Monitoring System</title>
<div class="scale-80 sm:scale-100 md:scale-100 origin-center">
    <div class="flex flex-col items-center justify-center min-h-screen pb-16">
        <div class="flex flex-row items-center justify-center space-x-5">
            <img src="/logo.png" alt="logo.png" class="w-11" />
            <div class="flex flex-col items-left justify-center">
                <h1 class="flex inter-h1 text-3xl">Train Station</h1>
                <h1 class="flex inter-h1 text-3xl">Monitoring System</h1>
            </div>
        </div>

        <br>

        <div class="flex-col justify-center align-center space-x-4 space-y-3 w-90">
            <input type="text" id="username" bind:value={username} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 inter-body" placeholder="Username" required />
            <input type="password" id="password" bind:value={password} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 inter-body toggle-password-active:hidden" placeholder="Password" required />
            <button
                class="max-w-sm mx-auto bg-blue-600 hover:bg-blue-700 text-white inter-body text-sm w-full py-2 px-4 rounded"
                on:click={login}
            >
                Login
            </button>
        </div>

        {#if loginFail}
            <p class="mt-4 text-red-500 inter-body">{loginFail}</p>
        {/if}
    </div>
</div>  