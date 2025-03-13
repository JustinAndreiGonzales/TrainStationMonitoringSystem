import { test, expect, defineConfig } from '@playwright/test';

export default defineConfig({
  retries: 2,
})

test('working station - lrt1', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.waitForSelector('#train-lines', {state: 'visible'})
  await page.locator('#train-lines').selectOption({label: 'LRT1'});
  await page.waitForSelector('#stations', {state: 'visible'})
  await page.locator('#stations').selectOption({label: 'United Nations'});

  const button = page.getByRole('button')
  await expect(button).toBeEnabled();
  await button.click();

  await expect(page).toHaveURL("https://trenph.vercel.app/stations?id=13");
});


test('working station - lrt2', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.waitForSelector('#train-lines', {state: 'visible'})
  await page.locator('#train-lines').selectOption({label: 'LRT2'});
  await page.waitForSelector('#stations', {state: 'visible'})
  await page.locator('#stations').selectOption({label: 'Katipunan'});

  const button = page.getByRole('button')
  await expect(button).toBeEnabled();
  await button.click();

  await expect(page).toHaveURL("https://trenph.vercel.app/stations?id=30");
});


test('working station - mrt3', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.waitForSelector('#train-lines', {state: 'visible'})
  await page.locator('#train-lines').selectOption({label: 'MRT3'});
  await page.waitForSelector('#stations', {state: 'visible'})
  await page.locator('#stations').selectOption({label: 'Ortigas'});

  const button = page.getByRole('button')
  await expect(button).toBeEnabled();
  await button.click();

  await expect(page).toHaveURL("https://trenph.vercel.app/stations?id=39");
});


test('non-operational station', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations');

  await page.locator('#train-lines').selectOption({label: 'LRT2'});
  await page.locator('#stations').selectOption({label: 'Recto'});
  await page.getByRole('button').click();

  await expect(page.getByText(/Error/)).toBeVisible;
});

