import { test, expect, defineConfig } from '@playwright/test';

export default defineConfig({
  retries: 2,
})

test('announcements viewable', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/admin');

  await page.getByPlaceholder('Username').fill('admin');
  await page.getByPlaceholder('Password').fill('password');

  await page.getByRole('button').click();
  await page.waitForNavigation();

  await page.goto('https://trenph.vercel.app/admin/announcements');

  expect(page.locator("Posted by: admin")).toBeTruthy();
});

test('announcements not postable', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/admin');

  await page.getByPlaceholder('Username').fill('admin');
  await page.getByPlaceholder('Password').fill('password');

  await page.getByRole('button').click();
  await page.waitForNavigation();

  await page.goto('https://trenph.vercel.app/admin/announcements');

  await page.getByPlaceholder('Subject').fill('sample subject');

  await expect(page.getByText('Submit')).toBeDisabled();
});


test('announcements postable', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/admin');

  await page.getByPlaceholder('Username').fill('admin');
  await page.getByPlaceholder('Password').fill('password');

  await page.getByRole('button').click();
  await page.waitForNavigation();

  await page.goto('https://trenph.vercel.app/admin/announcements');

  await page.getByPlaceholder('Subject').fill('test1');
  await page.getByPlaceholder('Body').fill('test2');
  await page.getByText('Submit').click();

  expect(page.getByText("Announcement has been posted successfully!"));
});