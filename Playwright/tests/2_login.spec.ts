import { test, expect } from '@playwright/test';

const url = 'https://trenph.vercel.app/admin';

test.beforeEach(async ({ page }) => {
  test.setTimeout(120_000)

  await page.goto(url);
});

test('login bad - no acc', async ({ page }) => {
  await page.getByPlaceholder('Username').fill('user');
  await page.getByPlaceholder('Password').fill('pw');

  await page.getByRole('button').click();

  await page.isVisible("text='Invalid credentials'");
});

test('login bad - wrong pw', async ({ page }) => {
  await page.getByPlaceholder('Username').fill('admin');
  await page.getByPlaceholder('Password').fill('pw');

  await page.getByRole('button').click();

  await page.isVisible("text='Invalid credentials'");
});

test('login bad - wrong user', async ({ page }) => {
  await page.getByPlaceholder('Username').fill('user');
  await page.getByPlaceholder('Password').fill('password');

  await page.getByRole('button').click();

  await page.isVisible("text='Invalid credentials'");
});

test('login ok', async ({ page }) => {
  await page.getByPlaceholder('Username').fill('admin');
  await page.getByPlaceholder('Password').fill('password');

  await page.getByRole('button').click();
  await page.waitForNavigation();

  await expect(page).toHaveURL("https://trenph.vercel.app/admin/home");

});
