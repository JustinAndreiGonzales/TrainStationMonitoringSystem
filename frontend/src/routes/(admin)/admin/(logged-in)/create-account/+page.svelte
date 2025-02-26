<script>
    import Button from '$lib/StandardButton.svelte';
    // add script with API
</script>


<title>Create account | Train Station Monitoring System</title>

<!-- IF ELSE DEPENDING ON ACCT CREDENTIALS -->
<!-- fix: centering -->
<h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Create account</h1>
<div class="scale-80 sm:scale-100 md:scale-100 origin-center scale-80 sm:scale-100 md:scale-100 ">
    <div class="flex flex-col items-center justify-center min-h-screen pb-16">  
        <div class="flex-col justify-center space-x-4 space-y-3">
            <input type="text" id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 inter-body" placeholder="Username" required />
            <input type="password" id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 inter-body toggle-password-active:hidden" placeholder="Password" required />
            <Button src="" text="Create account" href="/admin/create-account" />
            <!-- UPDATE TO POP UP -->
        </div>
    </div>
    <p> hello </p>
</div>