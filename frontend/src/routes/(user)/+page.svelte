<script>
    import Button from '$lib/StandardButton.svelte';
</script>

<div class="scale-80 sm:scale-100 md:scale-100 origin-center">
    <title>Train Station Monitoring System</title>
    <div class="flex flex-col items-center justify-center min-h-screen pb-16">
        <div class="flex flex-row items-center justify-center space-x-5">
            <img src="/logo.png" alt="logo.png" class="w-11" />
            <div class="flex flex-col items-left justify-center">
                <h1 class="flex inter-h1 text-3xl">Train Station</h1>
                <h1 class="flex inter-h1 text-3xl">Monitoring System</h1>
            </div>
        </div>

        <br>

        <div class="flex justify-center space-x-4">
            <Button src="/c.png" text="View station" href="/stations" />
            <Button src="/d.png" text="Determine route" href="/routes" />
        </div>
    </div>
</div>