import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export function load({ cookies }) {
  const role = cookies.get('role');

  if (role != 'superAdmin') {
    throw redirect(302, '/admin/home');
  }

  return {};
}
