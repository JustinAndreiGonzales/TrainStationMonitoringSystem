import { test, expect } from '@playwright/test';

test('routing page', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/');
  
    await page.getByText('Routes').click();
  
    await expect(page).toHaveURL("https://trenph.vercel.app/routes");
  });

test('VALID ROUTE - lrt2 to lrt2', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/routes');

    await page.locator('#train-lines1').selectOption({label: 'LRT2'});
    await page.locator('#stations1').selectOption({label: 'Katipunan'});

    await page.locator('#train-lines2').selectOption({label: 'LRT2'});
    await page.locator('#stations2').selectOption({label: 'Araneta-Cubao'});
  
    await expect(page.getByRole('button')).toBeVisible();

    await page.getByRole('button').click();
    
    await page.isVisible("text='Php 15'");

    await expect(page).toHaveURL("https://trenph.vercel.app/routes?start=30&end=28");
    //await expect(page.getByText('Php 15')).toBeVisible()
  });   

test('Missing Input - 1st', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/routes');

    await page.locator('#train-lines1').selectOption({label: 'LRT2'});
    await page.locator('#stations1').selectOption({label: 'Katipunan'});
  
    await expect(page.getByRole('button')).not.toBeVisible();
  });

test('Missing Input - 2st', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/routes');

    await page.locator('#train-lines2').selectOption({label: 'LRT2'});
    await page.locator('#stations2').selectOption({label: 'Katipunan'});
  
    await expect(page.getByRole('button')).not.toBeVisible();
  });

test('INVALID ROUTE - same station', async ({ page }) => {
    await page.goto('https://trenph.vercel.app/routes');

    await page.locator('#train-lines1').selectOption({label: 'LRT2'});
    await page.locator('#stations1').selectOption({label: 'Katipunan'});

    await page.locator('#train-lines2').selectOption({label: 'LRT2'});
    await page.locator('#stations2').selectOption({label: 'Katipunan'});
  
    await expect(page.getByRole('button')).not.toBeVisible();
  });