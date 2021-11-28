uint3 get_color(int iteration)
{
    int idx = iteration % 16;
    switch (idx) 
    {
        case 0: return (uint3)(66, 30, 15);
        case 1: return (uint3)(25, 7, 26);
        case 2: return (uint3)(9, 1, 47);
        case 3: return (uint3)(4, 4, 73);
        case 4: return (uint3)(0, 7, 100);
        case 5: return (uint3)(12, 44, 138);
        case 6: return (uint3)(24, 82, 177);
        case 7: return (uint3)(57, 125, 209);
        case 8: return (uint3)(134, 181, 229);
        case 9: return (uint3)(211, 236, 248);
        case 10: return(uint3)(241, 233, 191);
        case 11: return(uint3)(248, 201, 95);
        case 12: return(uint3)(255, 170, 0);
        case 13: return(uint3)(204, 128, 0);
        case 14: return(uint3)(153, 87, 0);
        case 15: return(uint3)(106, 52, 3);
    }
}


kernel void mandelbrot_set(float x_min, 
                           float x_max,
                           float y_min,
                           float y_max,
                           int max_iter,
                           write_only image2d_t out)
{
    const size_t width = get_global_size(0);
    const size_t height = get_global_size(1);

    const size_t col = get_global_id(0);
    const size_t row = get_global_id(1);
    
    float x_0 = x_min + (x_max - x_min) / width * col;
    float y_0 = y_min + (y_max - y_min) / height * row;

    float x = 0;
    float y = 0;

    int iteration = 0;
    
    while (x * x + y * y <= 4 && iteration < max_iter)
    {
        float x_temp = x * x - y * y + x_0;
        y = 2 * x * y + y_0;
        x = x_temp;
        iteration++;
    }  

    if (x * x + y * y <= 4)
    {
        write_imageui(out, (int2)(col, row), (uint4)(0, 0, 0, 255));
    }
    else
    {
        write_imageui(out, (int2)(col, row), (uint4)(get_color(iteration), 255));
    }
}

