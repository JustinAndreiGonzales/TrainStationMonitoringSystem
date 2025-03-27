import { test, expect, defineConfig } from '@playwright/test';

export default defineConfig({
  retries: 2,
})

test('eta not available', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/stations?id=1');

    let selected = page.getByTestId("eta").locator("Service is currently unavailable.");

    expect(selected).toBeTruthy();
  });

test('eta available - left', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations?id=2');

  let selected1 = page.getByTestId("eta").locator("min left")  ;
  let selected2 = page.getByTestId("eta").locator("mins left");
  let selected3 = page.getByTestId("eta").locator("Train has arrived!");

  expect(selected1 || selected2 || selected3).toBeTruthy();
});


test('eta available - right', async ({ page }) => {
  await page.goto('https://trenph.vercel.app/stations?id=3');

  await page.getByTestId("eta").getByText("Right").click();

  let selected1 = page.getByTestId("eta").locator("min left")  ;
  let selected2 = page.getByTestId("eta").locator("mins left");
  let selected3 = page.getByTestId("eta").locator("Train has arrived!");

  expect(selected1 || selected2 || selected3).toBeTruthy();
});