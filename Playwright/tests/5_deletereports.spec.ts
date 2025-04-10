import { test, expect, defineConfig } from '@playwright/test';

export default defineConfig({
  retries: 2,
})

const url = 'https://trenph.vercel.app/admin';
const user = 'admin';
const pw = 'password';

test.beforeEach(async ({ page }) => {
  await page.goto(url);

  await page.getByPlaceholder('Username').fill(user);
  await page.getByPlaceholder('Password').fill(pw);

  await page.getByRole('button').click();

  await page.getByText('Reports').click();
});

test('successful delete', async ({ page }) => {
  await page.locator('[aria-label="delete"]').first().click();
  await page.locator('[aria-label="confirm"]').click();
  
  await expect(page.getByText('Report has been successfully submitted!')).toBeTruthy();
});


test('cancel delete', async ({ page }) => {
  await page.locator('[aria-label="delete"]').first().click();
  await page.locator('[aria-label="cancel"]').click();
  
  await expect(page).toBeTruthy();
});
