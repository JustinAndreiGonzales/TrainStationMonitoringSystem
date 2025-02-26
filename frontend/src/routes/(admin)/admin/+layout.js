import { redirect } from '@sveltejs/kit';

export async function load({ fetch, url }) {
    const res = await fetch('/admin');
    const { isLoggedIn } = await res.json();

    if (!isLoggedIn && url.pathname !== '/admin') {
        throw redirect(303, '/admin');
    }

    return { isLoggedIn };
}
