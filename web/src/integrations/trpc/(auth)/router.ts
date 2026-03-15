import { z } from 'zod'
import { publicProcedure } from '../init'
import axiosInstance from '#/lib/axios'

const authRouter = {
  register: publicProcedure
    .input(
      z.object({
        email: z.email(),
        password: z.string().min(6),
      }),
    )
    .mutation(async ({ input }) => {
      try {
        const { data } = await axiosInstance.post('/auth/register/', input)
        return data
      } catch (error: any) {
        throw new Error(error.message)
      }
    }),
  login: publicProcedure
    .input(z.object({ email: z.email(), password: z.string() }))
    .mutation(async ({ input }) => {
      const res = await axiosInstance.post('/auth/login/', input)
      return res.data
    }),
}

export default authRouter;