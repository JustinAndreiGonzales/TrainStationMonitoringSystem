<script>   
    import Popup from "$lib/Popup.svelte";

    let username = '';
    let email = '';
    let password = '';
    let confirmPW = '';
    let role = '';

    let result = '';
    let submitted = false;

    const validUser = () => {
        const pattern = /^[\w.@+-]+$/;

        return (
            username.length > 0 &&
            username.length <= 150 &&
            pattern.test(username)
        );
    }

    const validEmail = () => {
        return email.match(
        /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
    };


    $: credsPass = email !== "" ? validUser() && role && password && eqPass && validEmail() : validUser() && role && password && eqPass;
    $: eqPass = (password === confirmPW);

    async function createAccount() {
        if(!submitted) {
            submitted = true;
            const res = await fetch('https://trenph.up.railway.app/api/signup/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                username: username,
                email: email,
                role: role,
                password: password,
                })  
            });

            if (!res.ok) {
                result = 'Error! No database connection';
            }
            else {
                result = 'Account has been successfully created!';
            } 

        }
    }
</script>


<title>Create account | Train Station Monitoring System</title>
<div class="scale-80 sm:scale-100 md:scale-100">
    <div class="flex flex-col items-center min-h-screen pb-16">
        <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Create account</h1>
        <br>
        <div class="flex-col justify-center align-center space-x-4 space-y-3 w-100">
            <label for="username" class="block mb-2 text-sm font-medium text-gray-900 inter-h2">
                Username*
            </label>  
            <input type="text" id="username" bind:value={username} class="bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 inter-body" placeholder="" required />
            {#if !validUser() && username}
                <p class="text-red-500 inter-body text-[12px] my=[-2px]">Username must be 150 characters or fewer. Use only letters, digits or @ . + - _.</p>
            {/if}

            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 inter-h2">
                Email address
            </label>  
            <input type="text" id="email" bind:value={email} class="bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 inter-body" placeholder="" />
            {#if !validEmail() && email}
                <p class="text-red-500 inter-body text-[12px] my=[-2px]">Email must be a valid address.</p>
            {/if}

            <label for="role" class="block mb-2 text-sm font-medium text-gray-900 inter-h2">
                Select account role*
            </label>  
            <form class="w-full">
                <select
                id="role"
                class={`inter-body bg-gray-50 border border-gray-300 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full py-2.5 px-1.5 ${role === '' ? 'text-gray-500' : 'text-gray-900'}`}
                bind:value={role}
                >
                    <option value="" selected class="text-gray-500"></option>
                    <option value="admin">Admin</option>
                    <option value="superAdmin">Super Admin</option>
                </select>
            </form>

            <label for="role" class="block mb-2 text-sm font-medium text-gray-900 inter-h2">
                Password*
            </label>  
            <input type="password" id="password" bind:value={password} class="bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 inter-body toggle-password-active:hidden" placeholder="" required />

            <label for="role" class="block mb-2 text-sm font-medium text-gray-900 inter-h2">
                Confirm password*
            </label>  
            <input type="password" id="password2" bind:value={confirmPW} class="bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 inter-body toggle-password-active:hidden" placeholder="" required />
            {#if !eqPass && (password && confirmPW)}
                <p class="text-red-500 inter-body text-[12px] my=[-2px]">Passwords do not match!</p>
            {/if}
            
            {#if credsPass}
                <button
                    class="w-full mt-3 mx-auto bg-blue-600 hover:bg-blue-700 text-white inter-body text-sm w-full py-2 px-4 rounded"
                    on:click={createAccount}
                >
                    Create account
                </button>
            {:else}
                <button
                    class="w-full mt-3 mx-auto bg-gray-300 text-white inter-body text-sm w-full py-2 px-4 rounded"
                    disabled
                >
                    Create account
                </button>
            {/if}
            
        </div>
    </div>
</div>  

{#if result}
    {#if result.includes("Error!")}
        <Popup message={result} href={"/admin/home"} text={"✕"} />
    {:else}
        <Popup message={result} href={"/admin/create-account"} text={"✕"} color="bg-green-700" txtColor="text-green-700" />
    {/if}
{/if}