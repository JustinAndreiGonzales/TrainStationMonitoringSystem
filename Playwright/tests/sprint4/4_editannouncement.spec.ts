import { test, expect, defineConfig } from '@playwright/test';

export default defineConfig({
  retries: 2,
})


test('announcements not editable', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/admin');

  await page.getByPlaceholder('Username').fill('admin');
  await page.getByPlaceholder('Password').fill('password');

  await page.getByRole('button').click();
  await page.waitForNavigation();

  await page.goto('https://trenph.vercel.app/admin/announcements');

  await page.getByText('Edit').first().click();
  await page.getByPlaceholder('Subject').fill('changed subject');

  await expect(page.getByText('Submit')).toBeDisabled();
});

test('announcements editable', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/admin');

  await page.getByPlaceholder('Username').fill('admin');
  await page.getByPlaceholder('Password').fill('password');

  await page.getByRole('button').click();
  await page.waitForNavigation();

  await page.goto('https://trenph.vercel.app/admin/announcements');

  await page.getByText('Edit').first().click();
  await page.getByPlaceholder('Subject').fill('changed subject');
  await page.getByPlaceholder('Body').fill('changed body');
  await page.getByText('Submit').click();

  expect(page.getByText("Announcement has been edited successfully!"));
});