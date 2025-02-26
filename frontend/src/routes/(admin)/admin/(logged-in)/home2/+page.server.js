export async function load({ cookies }) {
    const token = cookies.get('admin_auth');
    console.log(token);
    if (!token) {
        return { error: 'Not authenticated' };
    }

    try {
        // REPLACE: fetch url
        const res = await fetch('https://trenph.up.railway.app/api/reports/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            credentials: 'include'
        });

        if (res.ok) {
            const data = await res.json();
            return { data };
        }

        return { error: 'Failed to fetch data' };
    } catch (err) {
        return { error: 'Network error' };
    }
}
